# Decision Report

- generated_at: 2026-08-30T06:31:22.545247+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13028**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13028, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 14/18 | 77.8% | +1.87% | **+1.45%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.22% | **+0.89%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.73% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_10PCT | 4/20 | 20.0% | +1.36% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.12% | **+1.56%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.03% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$793.04** / 初期 $100.00 (+693.04%)
- 確定: 4798件 (Win 1462 / Loss 1578 / Flat 1758) / skip 4791件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $793.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.69** / 初期 $100.00 (+73.69%)
- 確定: 2112件 (Win 591 / Loss 515 / Flat 1006) / skip 4327件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0473 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $173.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.42** / 初期 $100.00 (+17.42%)
- 確定: 2071件 (Win 609 / Loss 803 / Flat 659) / pending 5件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000274 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $117.42

## 6. Latest Market Context

- 更新: 2026-08-30T06:31:11.108794+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78153.6
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +77.63% | $35,312,764.69 |
| NIULAI/USDT:USDT | +68.40% | $2,792,781.62 |
| PONS/USDT:USDT | +58.34% | $1,599,713.80 |
| FONE/USDT:USDT | +52.42% | $1,442,457.64 |
| SKR/USDT:USDT | +31.42% | $1,915,182.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MOVR/USDT:USDT | below_1h_threshold | +4.68% | +4.62% |
| NIULAI/USDT:USDT | below_1h_threshold | +4.67% | +4.62% |
| UAI/USDT:USDT | below_1h_threshold | +2.99% | +2.93% |
| 4/USDT:USDT | below_1h_threshold | +1.65% | +1.59% |
| ZKP/USDT:USDT | below_1h_threshold | +1.30% | +1.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
