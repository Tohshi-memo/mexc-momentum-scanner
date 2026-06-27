# Decision Report

- generated_at: 2026-06-27T18:08:50.265614+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7709**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7709, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.56% | **+0.36%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.63% | **+0.17%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.55% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.03% | **+1.03%** |
| ASK_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.67% | **+0.43%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.20** / 初期 $100.00 (+137.20%)
- 確定: 2219件 (Win 665 / Loss 739 / Flat 815) / skip 2051件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $237.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.06** / 初期 $100.00 (+7.06%)
- 確定: 440件 (Win 117 / Loss 112 / Flat 211) / skip 680件
- 成長率目線: 平均log +0.000155 / 幾何平均 +0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0293 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.06

## 5. Latest Market Context

- 更新: 2026-06-27T18:08:43.798882+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=60481.4
- Funnel: target 806 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +19.93% | $11,759,019.69 |
| S/USDT:USDT | +13.24% | $1,416,753.72 |
| BAS/USDT:USDT | +4.55% | $1,703,941.59 |
| RAVE/USDT:USDT | +3.26% | $3,718,680.46 |
| PI/USDT:USDT | +2.32% | $1,511,899.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| S/USDT:USDT | below_1h_threshold | +3.01% | +3.03% |
| ARX/USDT:USDT | below_1h_threshold | +1.92% | +1.95% |
| O/USDT:USDT | below_1h_threshold | +1.77% | +1.79% |
| BAS/USDT:USDT | below_1h_threshold | +1.76% | +1.78% |
| RE/USDT:USDT | below_1h_threshold | +1.75% | +1.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
