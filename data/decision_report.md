# Decision Report

- generated_at: 2026-06-18T09:49:40.399269+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7034**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7034, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.27% | **+0.17%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +5.70% | **+1.14%** |
| MARKET_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.42% | **+1.09%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.80% | **+0.81%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.70% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$217.88** / 初期 $100.00 (+117.88%)
- 確定: 1880件 (Win 530 / Loss 599 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XLM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $217.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.78** / 初期 $100.00 (+6.78%)
- 確定: 307件 (Win 89 / Loss 85 / Flat 133) / skip 138件
- 成長率目線: 平均log +0.000214 / 幾何平均 +0.021% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0601 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XLM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.78

## 5. Latest Market Context

- 更新: 2026-06-18T09:49:29.799474+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=64230.9
- Funnel: target 793 → liquid 171 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +76.13% | $44,129,978.18 |
| O/USDT:USDT | +66.49% | $4,541,276.83 |
| SYN/USDT:USDT | +63.23% | $6,081,526.86 |
| HOME/USDT:USDT | +44.70% | $2,439,304.69 |
| RE/USDT:USDT | +32.97% | $2,374,031.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.62% | +4.83% |
| HOME/USDT:USDT | below_1h_threshold | +4.45% | +4.66% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.14% | +4.35% |
| EVAA/USDT:USDT | below_1h_threshold | +2.97% | +3.18% |
| ALLO/USDT:USDT | below_1h_threshold | +2.73% | +2.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
