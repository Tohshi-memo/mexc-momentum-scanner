# Decision Report

- generated_at: 2026-08-25T07:41:45.309275+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12589**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12589, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.41%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 4/15 | 26.7% | +1.01% | **+0.27%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.03% | **+0.02%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.08% | **+2.00%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.78% | **+1.67%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.92% | **+1.34%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.01% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.23** / 初期 $100.00 (+616.23%)
- 確定: 4569件 (Win 1391 / Loss 1496 / Flat 1682) / skip 4581件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $716.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4023件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0675 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.07** / 初期 $100.00 (+16.07%)
- 確定: 1920件 (Win 564 / Loss 729 / Flat 627) / pending 6件 / skip 2137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000302 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.07

## 6. Latest Market Context

- 更新: 2026-08-25T07:41:31.437980+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=80507.4
- Funnel: target 1023 → liquid 177 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +76.30% | $1,015,873.67 |
| CATE/USDT:USDT | +68.52% | $4,419,032.45 |
| TAC/USDT:USDT | +44.69% | $5,014,251.45 |
| ONG/USDT:USDT | +33.97% | $4,947,768.80 |
| CASHCAT/USDT:USDT | +32.32% | $2,935,051.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +3.49% | +3.54% |
| JASMY/USDT:USDT | below_1h_threshold | +3.40% | +3.46% |
| RE/USDT:USDT | below_1h_threshold | +3.34% | +3.39% |
| MONAD/USDT:USDT | below_1h_threshold | +1.94% | +1.99% |
| FF/USDT:USDT | below_1h_threshold | +1.86% | +1.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
