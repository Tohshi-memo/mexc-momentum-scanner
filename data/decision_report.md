# Decision Report

- generated_at: 2026-05-28T14:26:08.375375+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4966**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4966, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.84% | **+0.55%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.59% | **+0.53%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.24% | **+0.23%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.96% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.08% | **+0.90%** |
| MARKET_LONG | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +0.00% | **+0.00%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 701件 (Win 172 / Loss 220 / Flat 309) / skip 826件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T14:26:05.736162+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=73039.1
- Funnel: target 776 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +34.20% | $11,386,130.76 |
| ESPORTS/USDT:USDT | +26.54% | $3,033,091.50 |
| ONDSSTOCK/USDT:USDT | +24.32% | $1,179,972.24 |
| XLM/USDT:USDT | +22.74% | $224,704,234.47 |
| PRL/USDT:USDT | +15.09% | $2,506,360.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.25% | +4.18% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.24% | +2.17% |
| DRAM/USDT:USDT | below_1h_threshold | +2.22% | +2.15% |
| LLYSTOCK/USDT:USDT | below_1h_threshold | +1.98% | +1.91% |
| JASMY/USDT:USDT | below_1h_threshold | +1.98% | +1.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
