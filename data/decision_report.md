# Decision Report

- generated_at: 2026-06-02T17:48:30.162509+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5477**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5477, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +4.27% | **+1.28%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +6.21% | **+0.93%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.65% | **+3.65%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| ASK_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.99% | **+0.74%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$97.10** / 初期 $100.00 (-2.90%)
- 確定トレード: 89件 (TP 26 / SL 60 / EXP 3)
- 最新: ENA/USDT:USDT SL_HIT PnL -3.88% 残高後 $97.10
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1062件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T17:48:27.347245+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=67437.9
- Funnel: target 770 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +33.86% | $11,208,919.23 |
| LIT/USDT:USDT | +14.32% | $3,241,383.17 |
| ENA/USDT:USDT | +12.80% | $37,187,634.50 |
| PIEVERSE/USDT:USDT | +10.01% | $5,609,951.60 |
| VVV/USDT:USDT | +8.21% | $7,193,022.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +4.97% | +4.90% |
| NEAR/USDT:USDT | below_1h_threshold | +4.28% | +4.21% |
| ENA/USDT:USDT | below_1h_threshold | +3.81% | +3.75% |
| LAB/USDT:USDT | below_1h_threshold | +3.56% | +3.49% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.48% | +3.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
