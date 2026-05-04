# Decision Report

- generated_at: 2026-05-04T16:52:56.216487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3237**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3237, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +2.66% | **+1.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +4.94% | **+1.48%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.87% | **+1.40%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.87% | **+0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +8.00% | **+4.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.80% | **+1.96%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.91% | **+1.62%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +3.33% | **+1.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T16:52:48.842588+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=80141.5
- Funnel: target 761 → liquid 205 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.3 >= 65=1, 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +15.44% | $35,562,315.56 |
| TST/USDT:USDT | +14.17% | $20,366,333.03 |
| TAG/USDT:USDT | +7.86% | $17,761,371.51 |
| FHE/USDT:USDT | +6.55% | $3,206,698.54 |
| B3/USDT:USDT | +5.19% | $1,014,803.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_relative_strength | +5.20% | +4.99% |
| AIOZ/USDT:USDT | below_1h_threshold | +3.93% | +3.72% |
| BIO/USDT:USDT | below_1h_threshold | +3.29% | +3.08% |
| GIGGLE/USDT:USDT | below_1h_threshold | +3.19% | +2.99% |
| BABY/USDT:USDT | below_1h_threshold | +2.64% | +2.43% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
