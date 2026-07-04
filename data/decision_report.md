# Decision Report

- generated_at: 2026-07-04T09:30:35.308393+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8240**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8240, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.29% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.48% | **+1.48%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$314.28** / 初期 $100.00 (+214.28%)
- 確定: 2557件 (Win 800 / Loss 853 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $314.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.51** / 初期 $100.00 (+6.51%)
- 確定: 636件 (Win 152 / Loss 155 / Flat 329) / skip 1015件
- 成長率目線: 平均log +0.000099 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0331 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.51

## 5. Latest Market Context

- 更新: 2026-07-04T09:30:26.171773+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=62453.9
- Funnel: target 834 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +76.86% | $5,227,543.92 |
| TLM/USDT:USDT | +58.56% | $44,049,946.02 |
| LAB/USDT:USDT | +57.05% | $53,948,167.57 |
| BAS/USDT:USDT | +38.84% | $4,401,722.23 |
| HMSTR/USDT:USDT | +33.83% | $6,173,943.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEX/USDT:USDT | below_1h_threshold | +4.72% | +4.84% |
| TLM/USDT:USDT | below_1h_threshold | +4.68% | +4.80% |
| DOGS/USDT:USDT | below_1h_threshold | +4.64% | +4.76% |
| H/USDT:USDT | below_1h_threshold | +1.82% | +1.94% |
| BSB/USDT:USDT | below_1h_threshold | +1.33% | +1.45% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
