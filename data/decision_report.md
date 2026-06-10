# Decision Report

- generated_at: 2026-06-10T19:06:24.596008+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6244**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6244, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_BB3S | 6/14 | 42.9% | -0.08% | **-0.03%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.25% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.24% | **+0.78%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.80% | **+0.54%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.20% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.49** / 初期 $100.00 (+50.49%)
- 確定: 1234件 (Win 308 / Loss 384 / Flat 542) / skip 1571件
- 成長率目線: 平均log +0.000331 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $150.49

## 4. Latest Market Context

- 更新: 2026-06-10T19:06:20.281121+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=61746.7
- Funnel: target 785 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +26.43% | $16,740,465.31 |
| FOLKS/USDT:USDT | +17.10% | $7,743,298.05 |
| ESPORTS/USDT:USDT | +10.59% | $24,944,593.20 |
| UAI/USDT:USDT | +8.64% | $1,991,196.21 |
| POWER/USDT:USDT | +7.14% | $1,668,381.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +2.56% | +2.72% |
| BTW/USDT:USDT | below_1h_threshold | +1.41% | +1.58% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.40% | +1.57% |
| VELVET/USDT:USDT | below_1h_threshold | +1.02% | +1.18% |
| H/USDT:USDT | below_1h_threshold | +0.94% | +1.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
