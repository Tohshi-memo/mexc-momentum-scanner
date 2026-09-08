# Decision Report

- generated_at: 2026-09-08T15:31:25.684178+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14007**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=14007, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.99% | **+0.35%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.06% | **+0.04%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.12% | **+0.02%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.28% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.67% | **+1.59%** |
| MARKET_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.49% | **+1.05%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.58% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,009.41** / 初期 $100.00 (+909.41%)
- 確定: 5271件 (Win 1585 / Loss 1707 / Flat 1979) / skip 5297件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,009.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.18** / 初期 $100.00 (+90.18%)
- 確定: 2610件 (Win 723 / Loss 622 / Flat 1265) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0386 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VVV/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.72** / 初期 $100.00 (+19.72%)
- 確定: 2596件 (Win 760 / Loss 984 / Flat 852) / pending 2件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000248 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VVV/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.72

## 6. Latest Market Context

- 更新: 2026-09-08T15:31:11.617940+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78428.6
- Funnel: target 1070 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +43.22% | $34,971,523.03 |
| VVV/USDT:USDT | +38.20% | $7,083,775.30 |
| USELESS/USDT:USDT | +33.23% | $18,676,096.23 |
| BNCSTOCK/USDT:USDT | +32.28% | $2,458,854.57 |
| AKE/USDT:USDT | +22.66% | $10,856,235.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOT/USDT:USDT | below_1h_threshold | +4.72% | +4.85% |
| BR/USDT:USDT | below_1h_threshold | +4.68% | +4.81% |
| VVV/USDT:USDT | below_1h_threshold | +4.46% | +4.59% |
| ADA/USDT:USDT | below_1h_threshold | +4.02% | +4.15% |
| ETC/USDT:USDT | below_1h_threshold | +3.57% | +3.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
