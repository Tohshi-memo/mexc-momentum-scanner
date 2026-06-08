# Decision Report

- generated_at: 2026-06-08T01:16:06.922488+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6014**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6014, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.57% | **-1.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.34% | **+0.40%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 2/16 | 12.5% | +0.90% | **+0.11%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.03% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.73% | **+1.91%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.08% | **+1.66%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.02% | **+1.11%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.18% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$155.03** / 初期 $100.00 (+55.03%)
- 確定: 1131件 (Win 277 / Loss 342 / Flat 512) / skip 1444件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $155.03

## 4. Latest Market Context

- 更新: 2026-06-08T01:16:04.567451+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.01% price=62954.2
- Funnel: target 772 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +27.19% | $86,639,293.79 |
| BANK/USDT:USDT | +26.66% | $4,454,991.38 |
| BLESS/USDT:USDT | +19.69% | $7,593,939.04 |
| PIPPIN/USDT:USDT | +18.47% | $6,139,048.06 |
| ESPORTS/USDT:USDT | +16.92% | $5,318,139.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +2.08% | +3.09% |
| USOIL/USDT:USDT | below_1h_threshold | +1.56% | +2.57% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.22% | +2.23% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +0.53% | +1.55% |
| B/USDT:USDT | below_1h_threshold | +0.49% | +1.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
