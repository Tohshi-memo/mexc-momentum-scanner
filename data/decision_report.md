# Decision Report

- generated_at: 2026-10-23T15:51:45.625944+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17238**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17238, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-3.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.22% | **-3.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 13/20 | 65.0% | +1.05% | **+0.68%** |
| LIMIT_7PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_9PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_8PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_10PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +5.85% | **+3.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.17% | **+2.92%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.43% | **+2.92%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +5.60% | **+2.80%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +6.50% | **+2.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7246件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$286.09** / 初期 $100.00 (+186.09%)
- 確定: 3902件 (Win 1068 / Loss 908 / Flat 1926) / skip 6747件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1821 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $286.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5399件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000490 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T15:51:22.294266+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=81606.1
- Funnel: target 1088 → liquid 170 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.2 >= 65=1, 4h RSI 84.9 >= 65=1, 4h RSI 70.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +179.22% | $35,030,823.19 |
| BIRB/USDT:USDT | +79.80% | $2,563,547.21 |
| BTR/USDT:USDT | +44.98% | $15,990,579.21 |
| UNITREE/USDT:USDT | +21.87% | $6,129,525.91 |
| DNA/USDT:USDT | +13.11% | $5,352,789.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +2.41% | +2.58% |
| BTR/USDT:USDT | below_1h_threshold | +2.20% | +2.38% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.44% |
| ATH/USDT:USDT | below_1h_threshold | +1.26% | +1.43% |
| DNA/USDT:USDT | below_1h_threshold | +1.08% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
