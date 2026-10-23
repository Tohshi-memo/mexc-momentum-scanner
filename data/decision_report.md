# Decision Report

- generated_at: 2026-10-23T15:36:43.052531+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17230**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17230, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.54% | **-2.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_7PCT | 5/20 | 25.0% | -0.24% | **-0.06%** |
| LIMIT_BB3S | 7/19 | 36.8% | -0.28% | **-0.10%** |
| LIMIT_5PCT | 11/20 | 55.0% | -0.21% | **-0.11%** |
| LIMIT_9PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +4.95% | **+2.47%** |
| MARKET_LONG | 20/20 | 100.0% | +2.34% | **+2.34%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.49% | **+1.99%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +4.90% | **+1.96%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.46% | **+1.73%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7238件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.10** / 初期 $100.00 (+180.10%)
- 確定: 3894件 (Win 1063 / Loss 905 / Flat 1926) / skip 6747件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1178 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $280.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5391件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000388 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T15:36:22.226171+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=81606.0
- Funnel: target 1088 → liquid 169 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.8 >= 65=1, 4h RSI 83.4 >= 65=1, 4h RSI 71.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +184.23% | $32,529,215.65 |
| BIRB/USDT:USDT | +63.73% | $2,166,273.57 |
| BTR/USDT:USDT | +46.79% | $15,895,021.24 |
| UNITREE/USDT:USDT | +22.01% | $6,124,939.29 |
| AKE/USDT:USDT | +13.46% | $16,358,173.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +3.48% | +3.65% |
| MVLL/USDT:USDT | below_1h_threshold | +2.41% | +2.58% |
| AKE/USDT:USDT | below_1h_threshold | +1.33% | +1.51% |
| KORU/USDT:USDT | below_1h_threshold | +0.85% | +1.03% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
