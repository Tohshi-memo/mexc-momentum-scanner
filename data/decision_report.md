# Decision Report

- generated_at: 2026-06-16T01:24:22.595461+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6825**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6825, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.00% | **-2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.23% | **+0.15%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.36% | **-0.09%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.54% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.58% | **+2.06%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.22% | **+1.93%** |
| MARKET_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| ASK_LONG | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.30% | **+1.48%** |

## 2. $100 Live Portfolio

- 残高: **$103.01** / 初期 $100.00 (+3.01%)
- 確定トレード: 9件 (TP 5 / SL 4 / EXP 0)
- 最新: ASTEROID/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.01
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.74** / 初期 $100.00 (+84.74%)
- 確定: 1698件 (Win 445 / Loss 528 / Flat 725) / skip 1688件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUFFER/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $184.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 81件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0439 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T01:24:16.889821+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=66317.0
- Funnel: target 772 → liquid 158 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.9 >= 65=1, 4h RSI 65.3 >= 65=1, 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +25.19% | $2,684,588.13 |
| ASTEROID/USDT:USDT | +25.15% | $6,902,521.58 |
| FOLKS/USDT:USDT | +23.18% | $2,583,885.18 |
| PUFFER/USDT:USDT | +22.89% | $1,186,678.30 |
| SPCXSTOCK/USDT:USDT | +21.62% | $371,619,007.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.33% | +3.18% |
| BSB/USDT:USDT | below_1h_threshold | +3.07% | +2.92% |
| ALLO/USDT:USDT | below_1h_threshold | +2.12% | +1.97% |
| VELVET/USDT:USDT | below_1h_threshold | +1.89% | +1.74% |
| SIREN/USDT:USDT | below_1h_threshold | +1.64% | +1.49% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
