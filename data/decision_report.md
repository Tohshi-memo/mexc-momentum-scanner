# Decision Report

- generated_at: 2026-07-22T12:26:17.120947+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9282**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=9282, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.84% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.09% | **+0.09%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.09% | **+0.06%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.03% | **-0.02%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$431.78** / 初期 $100.00 (+331.78%)
- 確定: 3279件 (Win 1035 / Loss 1053 / Flat 1191) / skip 2564件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $431.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1533件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1079 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.26** / 初期 $100.00 (+2.26%)
- 確定: 419件 (Win 142 / Loss 172 / Flat 105) / pending 2件 / skip 332件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000261 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $102.26

## 6. Latest Market Context

- 更新: 2026-07-22T12:26:10.844642+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=65830.3
- Funnel: target 888 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +40.56% | $3,376,869.49 |
| RE/USDT:USDT | +28.86% | $10,296,336.92 |
| SMCISTOCK/USDT:USDT | +16.13% | $4,644,848.39 |
| BNCSTOCK/USDT:USDT | +13.12% | $2,936,571.26 |
| ZAMA/USDT:USDT | +12.89% | $1,268,373.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INFQSTOCK/USDT:USDT | below_1h_threshold | +3.37% | +3.59% |
| ERA/USDT:USDT | below_1h_threshold | +2.33% | +2.56% |
| BANK/USDT:USDT | below_1h_threshold | +2.15% | +2.38% |
| BLESS/USDT:USDT | below_1h_threshold | +1.30% | +1.53% |
| BILL/USDT:USDT | below_1h_threshold | +0.99% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
