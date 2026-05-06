# Decision Report

- generated_at: 2026-05-06T15:12:34.691624+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3476**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3476, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.49% | **+0.60%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.97% | **+1.97%** |
| ASK_LONG | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.13% | **+0.79%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.04% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 28件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T15:12:31.990160+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=81444.4
- Funnel: target 770 → liquid 195 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +128.08% | $4,814,874.42 |
| LAB/USDT:USDT | +46.55% | $168,506,310.22 |
| IO/USDT:USDT | +35.71% | $15,473,622.50 |
| ZEC/USDT:USDT | +35.17% | $755,362,054.69 |
| BILL/USDT:USDT | +33.54% | $5,994,226.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_1h_threshold | +4.02% | +4.05% |
| LAB/USDT:USDT | below_1h_threshold | +3.79% | +3.82% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.30% | +1.34% |
| ZEC/USDT:USDT | below_1h_threshold | +1.05% | +1.09% |
| TAO/USDT:USDT | below_1h_threshold | +0.76% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
