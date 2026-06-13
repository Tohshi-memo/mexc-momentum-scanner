# Decision Report

- generated_at: 2026-06-13T15:02:46.280224+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6584**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6584, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.00% | **+0.00%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.12% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.77% | **+0.77%** |
| MARKET_LONG | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.12% | **+0.56%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.08% | **+0.54%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.77% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.68** / 初期 $100.00 (+64.68%)
- 確定: 1457件 (Win 390 / Loss 464 / Flat 603) / skip 1688件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $164.68

## 4. Latest Market Context

- 更新: 2026-06-13T15:02:43.449278+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64176.3
- Funnel: target 770 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COAI/USDT:USDT | +58.69% | $10,225,760.43 |
| JCT/USDT:USDT | +43.35% | $9,632,842.62 |
| RIF/USDT:USDT | +30.02% | $5,254,713.21 |
| TAO/USDT:USDT | +25.15% | $191,622,763.42 |
| EDGE/USDT:USDT | +17.67% | $3,406,978.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +1.93% | +1.94% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.70% | +0.72% |
| RIF/USDT:USDT | below_1h_threshold | +0.45% | +0.46% |
| JCT/USDT:USDT | below_1h_threshold | +0.42% | +0.43% |
| WLD/USDT:USDT | below_1h_threshold | +0.37% | +0.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
