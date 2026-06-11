# Decision Report

- generated_at: 2026-06-11T20:49:04.770596+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6405**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6405, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.18% | **+0.30%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.10% | **+0.73%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.96% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.39** / 初期 $100.00 (+53.39%)
- 確定: 1322件 (Win 344 / Loss 423 / Flat 555) / skip 1644件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $153.39

## 4. Latest Market Context

- 更新: 2026-06-11T20:48:58.576755+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.52% price=63245.8
- Funnel: target 782 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.6 >= 65=1, 4h RSI 76.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +85.25% | $119,907,758.22 |
| ESPORTS/USDT:USDT | +49.93% | $14,665,796.45 |
| NAORIS/USDT:USDT | +23.39% | $1,298,587.72 |
| UB/USDT:USDT | +16.21% | $1,703,667.06 |
| SKYAI/USDT:USDT | +10.72% | $12,465,434.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.99% | +5.50% |
| UB/USDT:USDT | below_1h_threshold | +2.92% | +3.44% |
| PYTH/USDT:USDT | below_1h_threshold | +2.59% | +3.11% |
| PLSTOCK/USDT:USDT | below_1h_threshold | +2.22% | +2.74% |
| BEAT/USDT:USDT | below_1h_threshold | +1.65% | +2.17% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
