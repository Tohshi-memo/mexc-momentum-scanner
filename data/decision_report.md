# Decision Report

- generated_at: 2026-09-26T03:56:29.740528+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15566**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15566, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/20 | 40.0% | +2.58% | **+1.03%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.98% | **+0.63%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.94% | **+1.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.52% | **+1.37%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,223.16** / 初期 $100.00 (+1123.16%)
- 確定: 5927件 (Win 1748 / Loss 1900 / Flat 2279) / skip 6200件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,223.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.10** / 初期 $100.00 (+156.10%)
- 確定: 3496件 (Win 957 / Loss 796 / Flat 1743) / skip 5481件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1024 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $256.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3185件 (Win 937 / Loss 1262 / Flat 986) / pending 1件 / skip 3851件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000349 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LDO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.03% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T03:56:16.116313+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=83914.5
- Funnel: target 1067 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARK/USDT:USDT | +22.51% | $3,054,369.63 |
| BR/USDT:USDT | +21.16% | $9,879,312.46 |
| H/USDT:USDT | +13.25% | $1,098,324.90 |
| BATON/USDT:USDT | +12.76% | $1,481,941.80 |
| PHA/USDT:USDT | +11.98% | $28,706,344.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +4.97% | +5.05% |
| LYN/USDT:USDT | below_1h_threshold | +4.62% | +4.70% |
| AVNT/USDT:USDT | below_1h_threshold | +1.93% | +2.01% |
| JTO/USDT:USDT | below_1h_threshold | +1.25% | +1.33% |
| ACE/USDT:USDT | below_1h_threshold | +1.18% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
