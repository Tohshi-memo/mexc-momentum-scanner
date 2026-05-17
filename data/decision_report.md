# Decision Report

- generated_at: 2026-05-17T05:23:23.776136+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4385**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4385, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +0.58% | **+0.12%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 9/18 | 50.0% | -0.27% | **-0.13%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.23% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.52% | **+0.99%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.76% | **+0.49%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.13% | **+0.47%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.74% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 553件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T05:23:20.348998+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78141.9
- Funnel: target 760 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CGPT/USDT:USDT | +32.20% | $1,684,825.83 |
| AIA/USDT:USDT | +26.47% | $6,402,138.26 |
| BSB/USDT:USDT | +14.56% | $4,376,794.72 |
| ASTEROID/USDT:USDT | +12.03% | $4,003,827.92 |
| AIGENSYN/USDT:USDT | +8.24% | $2,744,102.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CGPT/USDT:USDT | below_1h_threshold | +3.51% | +3.47% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.19% | +3.16% |
| INJ/USDT:USDT | below_1h_threshold | +1.20% | +1.16% |
| H/USDT:USDT | below_1h_threshold | +1.17% | +1.14% |
| RUNE/USDT:USDT | below_1h_threshold | +1.14% | +1.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
