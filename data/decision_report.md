# Decision Report

- generated_at: 2026-06-07T17:55:47.369992+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5991**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5991, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.56% | **-1.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.69% | **+3.79%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.60% | **+1.38%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.14% | **+1.29%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.53% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.13** / 初期 $100.00 (+51.13%)
- 確定: 1108件 (Win 268 / Loss 332 / Flat 508) / skip 1444件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $151.13

## 4. Latest Market Context

- 更新: 2026-06-07T17:55:41.974668+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=62145.1
- Funnel: target 768 → liquid 123 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +23.80% | $2,493,157.40 |
| PIPPIN/USDT:USDT | +8.27% | $2,702,496.78 |
| VELVET/USDT:USDT | +8.25% | $2,904,150.34 |
| BEAT/USDT:USDT | +7.94% | $52,919,576.08 |
| MYX/USDT:USDT | +7.63% | $2,187,899.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +4.52% | +4.38% |
| BTW/USDT:USDT | below_1h_threshold | +3.72% | +3.58% |
| BABY/USDT:USDT | below_1h_threshold | +1.90% | +1.76% |
| GRASS/USDT:USDT | below_1h_threshold | +1.52% | +1.38% |
| ASTER/USDT:USDT | below_1h_threshold | +0.90% | +0.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
