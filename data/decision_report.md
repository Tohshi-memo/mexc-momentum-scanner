# Decision Report

- generated_at: 2026-05-03T08:42:09.561469+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3055**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3055, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.54% | **+0.38%** |
| LIMIT_BB3S | 12/15 | 80.0% | +0.12% | **+0.10%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.39% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.33% | **+2.16%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.05% | **+1.98%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.62% | **+1.44%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.56% | **+1.32%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.74% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T08:42:07.047368+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78377.0
- Funnel: target 755 → liquid 164 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1, 4h RSI 97.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +70.95% | $11,308,462.33 |
| BR/USDT:USDT | +22.59% | $3,825,595.29 |
| AIGENSYN/USDT:USDT | +22.41% | $3,391,668.71 |
| B/USDT:USDT | +22.39% | $39,719,422.13 |
| TAC/USDT:USDT | +21.61% | $2,757,432.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +4.36% | +4.29% |
| AKT/USDT:USDT | below_1h_threshold | +3.99% | +3.92% |
| ALCH/USDT:USDT | below_1h_threshold | +3.79% | +3.71% |
| BSB/USDT:USDT | below_1h_threshold | +2.73% | +2.65% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.18% | +2.10% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
