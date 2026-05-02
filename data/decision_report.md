# Decision Report

- generated_at: 2026-05-02T04:27:02.774338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2860**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2860, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.35% | **+1.84%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.14% | **+1.73%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.84% | **+1.47%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.37% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T04:26:57.628455+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=78214.3
- Funnel: target 755 → liquid 172 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +124.73% | $37,307,275.28 |
| SKYAI/USDT:USDT | +18.61% | $21,557,951.70 |
| B/USDT:USDT | +17.51% | $72,759,386.78 |
| BSB/USDT:USDT | +11.82% | $11,212,912.89 |
| BLESS/USDT:USDT | +11.81% | $1,865,742.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.65% | +4.86% |
| B/USDT:USDT | below_1h_threshold | +3.65% | +3.86% |
| BR/USDT:USDT | below_1h_threshold | +1.53% | +1.74% |
| PLAY/USDT:USDT | below_1h_threshold | +1.34% | +1.54% |
| BEAT/USDT:USDT | below_1h_threshold | +1.18% | +1.39% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
