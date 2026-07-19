# Decision Report

- generated_at: 2026-07-19T16:11:15.923991+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9053**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=9053, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +1.90% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.62% | **+0.65%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.03% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.59% | **+1.25%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.45% | **+1.23%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | -0.28% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$395.33** / 初期 $100.00 (+295.33%)
- 確定: 3115件 (Win 977 / Loss 996 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PI/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $395.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.26** / 初期 $100.00 (+26.26%)
- 確定: 1014件 (Win 262 / Loss 216 / Flat 536) / skip 1450件
- 成長率目線: 平均log +0.000230 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0554 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $126.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.48** / 初期 $100.00 (+0.48%)
- 確定: 253件 (Win 86 / Loss 127 / Flat 40) / pending 3件 / skip 267件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000292 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PI/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.48

## 6. Latest Market Context

- 更新: 2026-07-19T16:11:11.267775+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64508.9
- Funnel: target 885 → liquid 126 → pre 50 → checked 48 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=2
- Strict後reject: 4h RSI 78.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +7.27% | $10,476,162.61 |
| BLESS/USDT:USDT | +3.84% | $1,846,880.33 |
| SLX/USDT:USDT | +3.02% | $1,084,626.16 |
| AKE/USDT:USDT | +2.17% | $48,668,138.89 |
| LAB/USDT:USDT | +1.81% | $6,337,113.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.85% | +3.90% |
| SLX/USDT:USDT | below_1h_threshold | +3.02% | +3.08% |
| AKE/USDT:USDT | below_1h_threshold | +2.19% | +2.24% |
| LAB/USDT:USDT | below_1h_threshold | +1.94% | +2.00% |
| BULLA/USDT:USDT | below_1h_threshold | +0.98% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
