# Decision Report

- generated_at: 2026-05-06T23:07:41.140546+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3508**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3508, expectancy=-0.15%
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
| LIMIT_FIB1272 | 5/20 | 25.0% | -1.31% | **-0.33%** |
| LIMIT_BB3S | 3/13 | 23.1% | -1.67% | **-0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.03% | **+1.83%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.20% | **+1.65%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +3.49% | **+1.50%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.67% | **+1.08%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.28% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 60件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T23:07:38.646292+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=81079.7
- Funnel: target 765 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +45.25% | $16,507,838.25 |
| ZEREBRO/USDT:USDT | +17.55% | $1,570,945.10 |
| BILL/USDT:USDT | +16.72% | $9,743,204.05 |
| LAB/USDT:USDT | +9.21% | $241,192,378.16 |
| DOGS/USDT:USDT | +8.28% | $5,200,865.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +0.71% | +0.97% |
| TAC/USDT:USDT | below_1h_threshold | +0.44% | +0.71% |
| SIREN/USDT:USDT | below_1h_threshold | +0.32% | +0.58% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +0.24% | +0.51% |
| ALBSTOCK/USDT:USDT | below_1h_threshold | +0.23% | +0.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
