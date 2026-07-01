# Decision Report

- generated_at: 2026-07-01T22:49:01.478281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8028**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8028, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.01% | **+0.30%** |
| LIMIT_10PCT | 8/20 | 40.0% | -0.14% | **-0.05%** |
| LIMIT_9PCT | 8/20 | 40.0% | -0.35% | **-0.14%** |
| ASK | 20/20 | 100.0% | -0.37% | **-0.37%** |
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.00% | **+3.00%** |
| ASK_LONG | 20/20 | 100.0% | +2.98% | **+2.98%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.01% | **+1.31%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.61% | **+0.31%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.97% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$294.88** / 初期 $100.00 (+194.88%)
- 確定: 2425件 (Win 748 / Loss 803 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $294.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.62** / 初期 $100.00 (+6.62%)
- 確定: 540件 (Win 136 / Loss 127 / Flat 277) / skip 899件
- 成長率目線: 平均log +0.000119 / 幾何平均 +0.012% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0361 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.62

## 5. Latest Market Context

- 更新: 2026-07-01T22:48:51.596666+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.54% price=60467.4
- Funnel: target 825 → liquid 158 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.6 >= 65=1, 4h RSI 94.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +237.93% | $38,893,128.02 |
| TLM/USDT:USDT | +119.15% | $4,474,869.82 |
| NOM/USDT:USDT | +25.01% | $5,613,464.41 |
| LIT/USDT:USDT | +18.11% | $8,807,821.69 |
| COOKIE/USDT:USDT | +17.06% | $1,086,484.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.30% | +4.84% |
| M/USDT:USDT | below_1h_threshold | +2.40% | +2.94% |
| CRV/USDT:USDT | below_1h_threshold | +1.67% | +2.22% |
| NOM/USDT:USDT | below_1h_threshold | +1.36% | +1.90% |
| ZEC/USDT:USDT | below_1h_threshold | +1.28% | +1.82% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
