# Decision Report

- generated_at: 2026-06-18T10:11:15.599599+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7036**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7036, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.05% | **+0.01%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.12% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +4.23% | **+1.06%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.40% | **+0.98%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.78% | **+0.89%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.94% | **+0.84%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.64% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$215.71** / 初期 $100.00 (+115.71%)
- 確定: 1882件 (Win 530 / Loss 601 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $215.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 139件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0517 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T10:11:10.209440+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=64023.5
- Funnel: target 793 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +72.07% | $6,377,402.00 |
| O/USDT:USDT | +70.30% | $4,681,778.85 |
| RE/USDT:USDT | +52.95% | $2,803,452.42 |
| ESPORTS/USDT:USDT | +45.23% | $45,149,056.23 |
| HOME/USDT:USDT | +37.19% | $2,553,844.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +2.22% | +2.46% |
| CLO/USDT:USDT | below_1h_threshold | +2.17% | +2.41% |
| EVAA/USDT:USDT | below_1h_threshold | +1.58% | +1.81% |
| O/USDT:USDT | below_1h_threshold | +1.53% | +1.76% |
| UP/USDT:USDT | below_1h_threshold | +1.39% | +1.63% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
