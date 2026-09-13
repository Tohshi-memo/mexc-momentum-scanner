# Decision Report

- generated_at: 2026-09-13T11:41:17.424093+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14424**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=14424, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.91% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.74% | **+0.67%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.00% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.92% | **+1.31%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.29% | **+1.10%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.50% | **+0.98%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.34% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5432件 (Win 1635 / Loss 1760 / Flat 2037) / skip 5553件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$226.35** / 初期 $100.00 (+126.35%)
- 確定: 2942件 (Win 818 / Loss 700 / Flat 1424) / skip 4893件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1088 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $226.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.16** / 初期 $100.00 (+27.16%)
- 確定: 2854件 (Win 850 / Loss 1103 / Flat 901) / pending 2件 / skip 3043件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000355 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FLOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $127.16

## 6. Latest Market Context

- 更新: 2026-09-13T11:41:08.909231+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=76750.0
- Funnel: target 1068 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +234.37% | $98,661,008.14 |
| STEEM/USDT:USDT | +54.84% | $1,978,337.14 |
| ARK/USDT:USDT | +49.91% | $1,627,078.78 |
| VTHO/USDT:USDT | +37.12% | $3,290,763.91 |
| POWR/USDT:USDT | +33.00% | $2,785,174.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARK/USDT:USDT | below_relative_strength | +5.08% | +4.94% |
| FLOCK/USDT:USDT | below_1h_threshold | +4.69% | +4.55% |
| UP/USDT:USDT | below_1h_threshold | +2.55% | +2.41% |
| REZ/USDT:USDT | below_1h_threshold | +2.13% | +1.99% |
| POWR/USDT:USDT | below_1h_threshold | +1.92% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
