# Decision Report

- generated_at: 2026-05-03T21:07:00.761249+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3106**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3106, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-2.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.73% | **-2.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_4PCT | 18/20 | 90.0% | +0.07% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +5.66% | **+3.39%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +4.03% | **+3.22%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.95% | **+2.66%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +4.95% | **+1.98%** |
| LIMIT_5PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T21:06:58.917606+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78898.1
- Funnel: target 755 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +60.33% | $283,256,967.15 |
| SKYAI/USDT:USDT | +21.30% | $26,699,140.76 |
| TAG/USDT:USDT | +16.25% | $3,976,692.81 |
| BSB/USDT:USDT | +10.78% | $14,938,178.15 |
| TST/USDT:USDT | +9.30% | $5,599,697.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +1.25% | +1.24% |
| BIO/USDT:USDT | below_1h_threshold | +1.12% | +1.11% |
| SPACE/USDT:USDT | below_1h_threshold | +1.04% | +1.03% |
| EDU/USDT:USDT | below_1h_threshold | +0.97% | +0.96% |
| GENIUS/USDT:USDT | below_1h_threshold | +0.88% | +0.87% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
