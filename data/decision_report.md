# Decision Report

- generated_at: 2026-05-03T18:51:53.287537+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3102**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3102, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.19% | **-2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.37% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 5/20 | 25.0% | +0.74% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +5.03% | **+3.27%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.23% | **+2.43%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +4.36% | **+2.18%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.36% | **+2.01%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T18:51:49.113406+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78718.7
- Funnel: target 755 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +56.23% | $319,774,161.54 |
| SKYAI/USDT:USDT | +16.10% | $25,561,042.42 |
| MERL/USDT:USDT | +9.97% | $1,019,452.17 |
| H/USDT:USDT | +8.17% | $8,803,406.46 |
| UB/USDT:USDT | +7.82% | $13,827,641.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +4.14% | +4.10% |
| MERL/USDT:USDT | below_1h_threshold | +3.63% | +3.60% |
| SIREN/USDT:USDT | below_1h_threshold | +3.53% | +3.49% |
| BB/USDT:USDT | below_1h_threshold | +3.29% | +3.26% |
| PNUT/USDT:USDT | below_1h_threshold | +3.24% | +3.21% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
