# Decision Report

- generated_at: 2026-05-06T14:02:37.144363+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3463**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3463, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.39% | **+0.66%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_BB3S | 6/15 | 40.0% | +0.32% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| MARKET_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.16% | **+0.75%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.67% | **+0.37%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.13% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 15件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T14:02:34.510737+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81531.8
- Funnel: target 770 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +87.89% | $3,230,013.00 |
| IO/USDT:USDT | +32.22% | $14,950,703.09 |
| BILL/USDT:USDT | +31.91% | $5,434,497.61 |
| ZEC/USDT:USDT | +31.42% | $755,375,658.77 |
| FHE/USDT:USDT | +31.29% | $33,090,448.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SMCISTOCK/USDT:USDT | below_1h_threshold | +0.98% | +1.09% |
| FHE/USDT:USDT | below_1h_threshold | +0.94% | +1.05% |
| JTO/USDT:USDT | below_1h_threshold | +0.79% | +0.90% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.51% | +0.62% |
| B3/USDT:USDT | below_1h_threshold | +0.36% | +0.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
