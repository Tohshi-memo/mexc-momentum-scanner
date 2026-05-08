# Decision Report

- generated_at: 2026-05-08T20:47:29.722124+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3822**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3822, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/17 | 47.1% | +1.36% | **+0.64%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.39% | **+0.29%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.34% | **+0.15%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.14% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.18% | **+0.59%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.25% | **+0.21%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.35% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 191件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T20:47:26.851798+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=80239.9
- Funnel: target 767 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +13.38% | $2,797,597.71 |
| CORE/USDT:USDT | +12.91% | $1,379,407.29 |
| SATO/USDT:USDT | +10.43% | $6,213,140.01 |
| OP/USDT:USDT | +9.74% | $21,976,945.33 |
| CHIP/USDT:USDT | +8.63% | $53,823,154.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OP/USDT:USDT | below_1h_threshold | +3.28% | +3.16% |
| JASMY/USDT:USDT | below_1h_threshold | +3.24% | +3.12% |
| ICP/USDT:USDT | below_1h_threshold | +2.92% | +2.80% |
| ENA/USDT:USDT | below_1h_threshold | +2.11% | +1.99% |
| ORDI/USDT:USDT | below_1h_threshold | +2.10% | +1.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
