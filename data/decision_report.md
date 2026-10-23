# Decision Report

- generated_at: 2026-10-23T17:16:25.411976+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17261**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17261, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 11/20 | 55.0% | +4.73% | **+2.60%** |
| LIMIT_9PCT | 10/20 | 50.0% | +4.40% | **+2.20%** |
| LIMIT_7PCT | 11/20 | 55.0% | +3.16% | **+1.74%** |
| LIMIT_10PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_6PCT | 12/20 | 60.0% | +0.98% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.90% | **+2.92%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.61% | **+2.61%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.46% | **+2.21%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.38% | **+2.20%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +5.88% | **+1.76%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7269件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$302.76** / 初期 $100.00 (+202.76%)
- 確定: 3925件 (Win 1083 / Loss 916 / Flat 1926) / skip 6747件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2514 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $302.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000612 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T17:16:12.857875+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=81726.8
- Funnel: target 1088 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +94.44% | $53,936,386.50 |
| KIMCHI/USDT:USDT | +15.03% | $1,807,024.82 |
| SOXS/USDT:USDT | +3.05% | $36,244,910.14 |
| AKE/USDT:USDT | +2.82% | $15,214,579.98 |
| AGT/USDT:USDT | +2.72% | $6,068,809.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +2.70% | +2.64% |
| BTW/USDT:USDT | below_1h_threshold | +1.47% | +1.42% |
| AGT/USDT:USDT | below_1h_threshold | +1.17% | +1.11% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.08% | +1.03% |
| PYTH/USDT:USDT | below_1h_threshold | +0.97% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
