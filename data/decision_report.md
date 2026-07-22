# Decision Report

- generated_at: 2026-07-22T09:26:32.955255+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9267**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9267, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/13 | 23.1% | +5.13% | **+1.18%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.42% | **+0.85%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +0.95% | **+0.81%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.33% | **+0.80%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$422.50** / 初期 $100.00 (+322.50%)
- 確定: 3265件 (Win 1028 / Loss 1047 / Flat 1190) / skip 2563件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $422.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1518件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1476 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定: 407件 (Win 140 / Loss 168 / Flat 99) / pending 6件 / skip 329件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000487 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $102.36

## 6. Latest Market Context

- 更新: 2026-07-22T09:26:22.394555+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=65999.9
- Funnel: target 888 → liquid 176 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 66.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +49.91% | $3,277,238.20 |
| RE/USDT:USDT | +26.93% | $5,796,989.72 |
| SMCISTOCK/USDT:USDT | +18.51% | $4,329,029.73 |
| BNCSTOCK/USDT:USDT | +13.89% | $2,914,266.50 |
| QNTSTOCK/USDT:USDT | +13.22% | $5,447,238.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_relative_strength | +5.01% | +4.94% |
| RE/USDT:USDT | below_1h_threshold | +3.50% | +3.43% |
| TLM/USDT:USDT | below_1h_threshold | +1.82% | +1.75% |
| UB/USDT:USDT | below_1h_threshold | +1.75% | +1.68% |
| US/USDT:USDT | below_1h_threshold | +1.41% | +1.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
