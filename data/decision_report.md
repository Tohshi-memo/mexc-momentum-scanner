# Decision Report

- generated_at: 2026-05-06T22:22:26.160548+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3506**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3506, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.99% | **+0.25%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.01% | **+0.01%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.09% | **-0.07%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.40% | **-0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +4.62% | **+2.31%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.03% | **+1.83%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.20% | **+1.65%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.67% | **+1.08%** |
| ASK_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 58件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T22:22:23.533547+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=81251.5
- Funnel: target 764 → liquid 190 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +52.13% | $14,750,508.85 |
| BILL/USDT:USDT | +16.63% | $8,860,700.78 |
| ZEREBRO/USDT:USDT | +13.71% | $1,440,442.28 |
| VVV/USDT:USDT | +8.89% | $6,713,997.53 |
| LAB/USDT:USDT | +8.83% | $240,342,084.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.64% | +2.94% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.63% | +0.93% |
| DOGS/USDT:USDT | below_1h_threshold | +0.51% | +0.81% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +0.51% | +0.81% |
| PANWSTOCK/USDT:USDT | below_1h_threshold | +0.28% | +0.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
