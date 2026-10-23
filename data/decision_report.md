# Decision Report

- generated_at: 2026-10-23T16:16:24.749227+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17244**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17244, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-3.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.40% | **-3.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_6PCT | 13/20 | 65.0% | +1.50% | **+0.98%** |
| LIMIT_7PCT | 10/20 | 50.0% | +1.48% | **+0.74%** |
| LIMIT_9PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_10PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +4.08% | **+3.87%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +5.03% | **+3.52%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +6.50% | **+2.60%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +5.33% | **+2.40%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +5.25% | **+2.36%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7252件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$294.28** / 初期 $100.00 (+194.28%)
- 確定: 3908件 (Win 1074 / Loss 908 / Flat 1926) / skip 6747件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2398 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $294.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5406件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000583 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T16:16:12.337234+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=81547.8
- Funnel: target 1088 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.2 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +6.80% | $1,800,270.68 |
| IRYS/USDT:USDT | +5.99% | $37,464,638.56 |
| JCT/USDT:USDT | +4.85% | $4,932,633.90 |
| DNA/USDT:USDT | +1.78% | $5,372,291.18 |
| SOXS/USDT:USDT | +1.45% | $37,215,987.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.27% | +4.40% |
| DNA/USDT:USDT | below_1h_threshold | +1.73% | +1.86% |
| BIRB/USDT:USDT | below_1h_threshold | +1.58% | +1.71% |
| BMT/USDT:USDT | below_1h_threshold | +1.20% | +1.32% |
| Q/USDT:USDT | below_1h_threshold | +1.16% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
