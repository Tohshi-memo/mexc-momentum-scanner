# Decision Report

- generated_at: 2026-06-27T07:31:05.821216+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7676**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7676, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.76% | **+0.08%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.29% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.70% | **+1.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |
| ASK_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.26% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.11** / 初期 $100.00 (+138.11%)
- 確定: 2201件 (Win 661 / Loss 733 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $238.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.22** / 初期 $100.00 (+8.22%)
- 確定: 407件 (Win 111 / Loss 102 / Flat 194) / skip 680件
- 成長率目線: 平均log +0.000194 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0953 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $108.22

## 5. Latest Market Context

- 更新: 2026-06-27T07:30:58.092227+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=60400.9
- Funnel: target 806 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +39.89% | $56,447,484.66 |
| MYX/USDT:USDT | +36.55% | $9,317,575.22 |
| PUNDIX/USDT:USDT | +20.36% | $6,087,880.32 |
| SYRUP/USDT:USDT | +19.23% | $1,530,100.40 |
| SLX/USDT:USDT | +17.08% | $10,744,183.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| G/USDT:USDT | below_1h_threshold | +3.15% | +3.06% |
| MYX/USDT:USDT | below_1h_threshold | +3.11% | +3.02% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.29% | +2.20% |
| W/USDT:USDT | below_1h_threshold | +2.14% | +2.04% |
| GRASS/USDT:USDT | below_1h_threshold | +2.08% | +1.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
