# Decision Report

- generated_at: 2026-05-03T08:57:04.881082+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3056**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3056, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.54% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 13/16 | 81.2% | -0.20% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.94% | **+2.36%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.64% | **+2.18%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.28% | **+1.64%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.90% | **+1.52%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.55% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T08:57:02.818151+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78357.9
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +64.21% | $12,061,217.14 |
| B/USDT:USDT | +30.91% | $41,396,516.52 |
| BR/USDT:USDT | +26.25% | $3,878,054.79 |
| AIGENSYN/USDT:USDT | +18.72% | $3,534,611.25 |
| FHE/USDT:USDT | +17.97% | $2,878,231.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_relative_strength | +5.05% | +4.99% |
| ALCH/USDT:USDT | below_1h_threshold | +4.14% | +4.08% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.12% | +4.07% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +3.82% | +3.77% |
| AKT/USDT:USDT | below_1h_threshold | +2.88% | +2.83% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
