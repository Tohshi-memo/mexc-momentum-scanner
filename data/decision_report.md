# Decision Report

- generated_at: 2026-06-23T03:53:47.176066+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7408**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7408, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.35% | **+0.05%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.68% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.02% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.39** / 初期 $100.00 (+137.39%)
- 確定: 2064件 (Win 614 / Loss 678 / Flat 772) / skip 1905件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $237.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 313件 (Win 89 / Loss 87 / Flat 137) / skip 506件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0039 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-23T03:53:39.019674+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=64020.1
- Funnel: target 809 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARX/USDT:USDT | +52.36% | $9,684,057.11 |
| CLO/USDT:USDT | +22.14% | $3,507,809.19 |
| FOLKS/USDT:USDT | +19.79% | $5,680,446.52 |
| LAB/USDT:USDT | +13.10% | $32,103,584.57 |
| BLESS/USDT:USDT | +11.26% | $16,780,845.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.88% | +4.10% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.10% | +2.33% |
| AERO/USDT:USDT | below_1h_threshold | +1.88% | +2.11% |
| LAYER/USDT:USDT | below_1h_threshold | +1.63% | +1.85% |
| BEAT/USDT:USDT | below_1h_threshold | +1.31% | +1.53% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
