# Decision Report

- generated_at: 2026-09-26T06:41:30.033810+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15578**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15578, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.04% | **-1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.08% | **+1.66%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.74% | **+1.65%** |
| MARKET_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,249.61** / 初期 $100.00 (+1149.61%)
- 確定: 5939件 (Win 1753 / Loss 1904 / Flat 2282) / skip 6200件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RARE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,249.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$262.67** / 初期 $100.00 (+162.67%)
- 確定: 3508件 (Win 965 / Loss 800 / Flat 1743) / skip 5481件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1010 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $262.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3185件 (Win 937 / Loss 1262 / Flat 986) / pending 1件 / skip 3862件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000376 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LDO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.03% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T06:41:18.569008+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=83890.6
- Funnel: target 1067 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +301.04% | $1,237,510.45 |
| BATON/USDT:USDT | +32.94% | $1,570,246.32 |
| ARK/USDT:USDT | +23.42% | $3,729,546.58 |
| RARE/USDT:USDT | +22.56% | $2,009,276.98 |
| AERO/USDT:USDT | +13.51% | $4,583,682.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CC/USDT:USDT | below_1h_threshold | +2.72% | +2.72% |
| QNT/USDT:USDT | below_1h_threshold | +2.39% | +2.40% |
| BR/USDT:USDT | below_1h_threshold | +2.35% | +2.35% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.28% | +2.28% |
| AVNT/USDT:USDT | below_1h_threshold | +2.07% | +2.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
