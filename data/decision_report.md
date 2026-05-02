# Decision Report

- generated_at: 2026-05-02T12:37:01.726294+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2902**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2902, expectancy=-0.14%
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
| LIMIT_5PCT | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.14% | **+0.11%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.17% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +4.80% | **+2.88%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.23% | **+2.42%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.44% | **+2.24%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T12:36:59.429495+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=78190.1
- Funnel: target 755 → liquid 169 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.6 >= 65=1, 4h RSI 70.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +217.76% | $127,242,597.04 |
| TAG/USDT:USDT | +41.50% | $5,369,058.64 |
| BIO/USDT:USDT | +30.26% | $2,216,679.83 |
| TAC/USDT:USDT | +24.81% | $2,015,244.43 |
| XNY/USDT:USDT | +21.67% | $1,001,207.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +4.16% | +4.05% |
| B/USDT:USDT | below_1h_threshold | +3.29% | +3.18% |
| LAB/USDT:USDT | below_1h_threshold | +3.15% | +3.04% |
| USTC/USDT:USDT | below_1h_threshold | +2.89% | +2.78% |
| BLESS/USDT:USDT | below_1h_threshold | +2.71% | +2.60% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
