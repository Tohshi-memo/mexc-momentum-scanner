# Decision Report

- generated_at: 2026-05-01T04:46:03.016689+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2753**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2753, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.99% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.06% | **+0.04%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.37% | **+1.35%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.32% | **+1.06%** |
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| ASK_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.47% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T04:45:58.752674+00:00 / 保存件数 197/288
- BTC: STAGNANT 1h -0.08% price=77018.7
- Funnel: target 760 → liquid 206 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1, 4h RSI 71.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +27.24% | $9,627,239.12 |
| BR/USDT:USDT | +26.50% | $17,251,738.47 |
| ZEREBRO/USDT:USDT | +22.18% | $1,956,577.78 |
| ASTEROID/USDT:USDT | +16.41% | $4,227,801.92 |
| GENIUS/USDT:USDT | +15.97% | $1,457,485.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.32% | +4.40% |
| BLUAI/USDT:USDT | below_1h_threshold | +3.08% | +3.17% |
| ZBT/USDT:USDT | below_1h_threshold | +2.84% | +2.92% |
| MONAD/USDT:USDT | below_1h_threshold | +2.11% | +2.19% |
| VINE/USDT:USDT | below_1h_threshold | +2.08% | +2.16% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
