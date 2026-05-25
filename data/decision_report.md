# Decision Report

- generated_at: 2026-05-25T01:34:39.500553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4837**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4837, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.22% | **+0.22%** |
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.07% | **+0.04%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.83% | **+0.54%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.54% | **+0.19%** |
| MARKET_LONG | 20/20 | 100.0% | +0.17% | **+0.17%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.29% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.79** / 初期 $100.00 (+21.79%)
- 確定: 643件 (Win 158 / Loss 205 / Flat 280) / skip 755件
- 成長率目線: 平均log +0.000307 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MYX/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.79

## 4. Latest Market Context

- 更新: 2026-05-25T01:34:37.374142+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=77121.3
- Funnel: target 764 → liquid 111 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +13.58% | $1,074,240.65 |
| EDU/USDT:USDT | +5.46% | $1,026,549.87 |
| SUPER/USDT:USDT | +4.91% | $3,561,738.04 |
| BILL/USDT:USDT | +4.84% | $14,823,332.75 |
| AGT/USDT:USDT | +3.58% | $7,277,733.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GENIUS/USDT:USDT | below_1h_threshold | +1.22% | +1.21% |
| SAGA/USDT:USDT | below_1h_threshold | +1.19% | +1.18% |
| NIL/USDT:USDT | below_1h_threshold | +1.05% | +1.04% |
| BILL/USDT:USDT | below_1h_threshold | +0.95% | +0.95% |
| BEAT/USDT:USDT | below_1h_threshold | +0.92% | +0.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
