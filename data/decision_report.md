# Decision Report

- generated_at: 2026-05-07T01:17:30.770389+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3519**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3519, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.03% | **+0.03%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.38% | **+2.14%** |
| MARKET_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| ASK_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.12% | **+1.41%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.01% | **+1.41%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$100.11** / 初期 $100.00 (+0.11%)
- 確定: 14件 (Win 3 / Loss 5 / Flat 6) / skip 66件
- 成長率目線: 平均log +0.000081 / 幾何平均 +0.008% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOGS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $100.11

## 4. Latest Market Context

- 更新: 2026-05-07T01:17:27.911293+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=81050.8
- Funnel: target 766 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +47.71% | $5,846,464.43 |
| PLAY/USDT:USDT | +18.37% | $19,308,768.36 |
| FHE/USDT:USDT | +17.43% | $15,558,504.34 |
| PENGUIN/USDT:USDT | +10.95% | $1,013,790.93 |
| VVV/USDT:USDT | +10.09% | $8,469,805.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +3.30% | +3.20% |
| NOT/USDT:USDT | below_1h_threshold | +2.66% | +2.56% |
| UB/USDT:USDT | below_1h_threshold | +1.33% | +1.23% |
| VVV/USDT:USDT | below_1h_threshold | +1.30% | +1.20% |
| SILVER/USDT:USDT | below_1h_threshold | +1.18% | +1.07% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
