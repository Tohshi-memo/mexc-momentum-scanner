# Decision Report

- generated_at: 2026-07-05T17:58:49.348903+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8343**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8343, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.22% | **-0.07%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.48% | **+1.48%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.38% | **+0.48%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$101.07** / 初期 $100.00 (+1.07%)
- 確定トレード: 65件 (TP 22 / SL 42 / EXP 1)
- 最新: MAGMA/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.94** / 初期 $100.00 (+221.94%)
- 確定: 2620件 (Win 832 / Loss 884 / Flat 904) / skip 2284件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $321.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1116件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T17:58:43.351390+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=62606.4
- Funnel: target 835 → liquid 149 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1, 4h RSI 67.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEROC0MPUTE/USDT:USDT | +36.68% | $1,231,385.02 |
| NES/USDT:USDT | +8.65% | $4,818,054.51 |
| TLM/USDT:USDT | +8.04% | $31,063,881.35 |
| VELVET/USDT:USDT | +7.27% | $14,840,283.11 |
| TRB/USDT:USDT | +7.10% | $1,640,315.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.49% | +4.50% |
| LAB/USDT:USDT | below_1h_threshold | +3.80% | +3.81% |
| TRB/USDT:USDT | below_1h_threshold | +3.65% | +3.66% |
| XTZ/USDT:USDT | below_1h_threshold | +3.24% | +3.25% |
| ARX/USDT:USDT | below_1h_threshold | +2.81% | +2.82% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
