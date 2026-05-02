# Decision Report

- generated_at: 2026-05-02T15:12:10.125216+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2924**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2924, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-3.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.12% | **-3.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_6PCT | 11/20 | 55.0% | +2.44% | **+1.34%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_BB3S | 9/18 | 50.0% | +0.99% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.40% | **+2.04%** |
| ASK_LONG | 20/20 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +4.34% | **+1.74%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +5.97% | **+1.49%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T15:12:08.124158+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78392.6
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +293.26% | $159,592,186.43 |
| TAG/USDT:USDT | +76.28% | $9,251,742.31 |
| BIO/USDT:USDT | +52.50% | $3,713,635.61 |
| SKYAI/USDT:USDT | +30.74% | $18,328,489.23 |
| SPACE/USDT:USDT | +26.78% | $1,484,154.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +2.40% | +2.38% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.93% | +1.91% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +1.02% | +1.00% |
| SPACE/USDT:USDT | below_1h_threshold | +0.83% | +0.81% |
| MONAD/USDT:USDT | below_1h_threshold | +0.76% | +0.74% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
