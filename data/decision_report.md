# Decision Report

- generated_at: 2026-05-08T20:07:42.301437+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3820**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3820, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/18 | 38.9% | +1.16% | **+0.45%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.42% | **+0.19%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.99% | **+0.44%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.53% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.28% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 189件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T20:07:39.483641+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80130.9
- Funnel: target 768 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +17.61% | $5,911,419.87 |
| COLLECT/USDT:USDT | +13.88% | $2,621,614.39 |
| CORE/USDT:USDT | +13.59% | $1,141,714.01 |
| CHIP/USDT:USDT | +9.82% | $52,569,794.76 |
| RKLBSTOCK/USDT:USDT | +8.59% | $2,439,996.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.75% | +2.76% |
| CORE/USDT:USDT | below_1h_threshold | +2.16% | +2.18% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.68% | +1.70% |
| MOVR/USDT:USDT | below_1h_threshold | +1.63% | +1.65% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
