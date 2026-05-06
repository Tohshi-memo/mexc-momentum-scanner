# Decision Report

- generated_at: 2026-05-06T21:12:18.306963+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3500**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3500, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/12 | 33.3% | +1.90% | **+0.63%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.50% | **+0.40%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.28% | **+0.21%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +4.62% | **+2.31%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.94% | **+0.89%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.01% | **+0.86%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.38% | **+0.83%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.54% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 52件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T21:12:15.785535+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=81376.6
- Funnel: target 764 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +50.55% | $12,130,678.74 |
| ZEREBRO/USDT:USDT | +10.68% | $1,282,087.37 |
| UB/USDT:USDT | +9.58% | $1,681,782.17 |
| LAB/USDT:USDT | +9.40% | $235,726,682.35 |
| SMCISTOCK/USDT:USDT | +7.77% | $5,753,601.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.45% | +3.46% |
| BILL/USDT:USDT | below_1h_threshold | +1.37% | +1.37% |
| SIREN/USDT:USDT | below_1h_threshold | +1.25% | +1.25% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.23% | +1.23% |
| UB/USDT:USDT | below_1h_threshold | +0.91% | +0.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
