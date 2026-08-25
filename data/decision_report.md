# Decision Report

- generated_at: 2026-08-25T07:11:22.530018+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12585**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12585, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.79% | **-0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/14 | 42.9% | +1.11% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.25% | **+0.09%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.07% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.46% | **+1.48%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.46% | **+1.48%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.52% | **+1.06%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.49% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$709.14** / 初期 $100.00 (+609.14%)
- 確定: 4565件 (Win 1390 / Loss 1496 / Flat 1679) / skip 4581件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $709.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4019件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0262 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.17** / 初期 $100.00 (+15.17%)
- 確定: 1916件 (Win 561 / Loss 729 / Flat 626) / pending 4件 / skip 2137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000252 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.17

## 6. Latest Market Context

- 更新: 2026-08-25T07:11:14.805553+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=80714.2
- Funnel: target 1021 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +62.74% | $4,371,577.53 |
| CASHCAT/USDT:USDT | +29.29% | $2,891,020.21 |
| ONG/USDT:USDT | +27.31% | $4,527,967.71 |
| TAC/USDT:USDT | +23.08% | $4,664,976.41 |
| PONS/USDT:USDT | +23.02% | $1,492,894.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +4.68% | +4.48% |
| PONS/USDT:USDT | below_1h_threshold | +2.96% | +2.76% |
| BR/USDT:USDT | below_1h_threshold | +2.52% | +2.32% |
| KORU/USDT:USDT | below_1h_threshold | +1.62% | +1.41% |
| DASH/USDT:USDT | below_1h_threshold | +1.21% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
