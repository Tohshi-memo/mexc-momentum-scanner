# Decision Report

- generated_at: 2026-06-07T18:53:49.742783+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5992**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5992, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.96% | **-0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.29% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.69% | **+3.79%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.87% | **+1.35%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.67% | **+1.09%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.16% | **+0.87%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.38** / 初期 $100.00 (+50.38%)
- 確定: 1109件 (Win 268 / Loss 333 / Flat 508) / skip 1444件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $150.38

## 4. Latest Market Context

- 更新: 2026-06-07T18:53:46.775978+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=62070.1
- Funnel: target 768 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +22.94% | $2,875,089.02 |
| EPIC/USDT:USDT | +15.39% | $1,071,732.09 |
| BTW/USDT:USDT | +9.00% | $14,378,815.20 |
| BABY/USDT:USDT | +7.77% | $3,296,634.54 |
| VELVET/USDT:USDT | +6.90% | $2,951,286.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.90% | +3.99% |
| BABY/USDT:USDT | below_1h_threshold | +3.51% | +3.61% |
| RIVER/USDT:USDT | below_1h_threshold | +2.75% | +2.85% |
| B/USDT:USDT | below_1h_threshold | +2.26% | +2.36% |
| PLAY/USDT:USDT | below_1h_threshold | +2.03% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
