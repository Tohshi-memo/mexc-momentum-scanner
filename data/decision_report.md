# Decision Report

- generated_at: 2026-05-17T13:33:26.743993+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4401**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4401, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.86% | **+0.57%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.38% | **+0.30%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.38% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.92% | **+1.44%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.55% | **+1.32%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.02% | **+1.02%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| MARKET_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.52** / 初期 $100.00 (+18.52%)
- 確定: 399件 (Win 103 / Loss 137 / Flat 159) / skip 563件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $118.52

## 4. Latest Market Context

- 更新: 2026-05-17T13:33:24.813709+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=78212.3
- Funnel: target 760 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +45.20% | $13,476,292.59 |
| AIA/USDT:USDT | +34.63% | $15,856,234.18 |
| CGPT/USDT:USDT | +18.47% | $2,430,805.25 |
| KAIA/USDT:USDT | +14.08% | $2,598,870.61 |
| VVV/USDT:USDT | +12.41% | $6,816,593.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.31% | +4.46% |
| VVV/USDT:USDT | below_1h_threshold | +2.75% | +2.90% |
| GUA/USDT:USDT | below_1h_threshold | +1.60% | +1.75% |
| AIA/USDT:USDT | below_1h_threshold | +1.38% | +1.52% |
| CHZ/USDT:USDT | below_1h_threshold | +1.07% | +1.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
