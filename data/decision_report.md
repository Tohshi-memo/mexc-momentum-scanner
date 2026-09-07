# Decision Report

- generated_at: 2026-09-07T07:11:20.617389+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13864**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.67% / filled 20/20。**
- 全期間 MARKET基準: n=13864, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.67% | **+1.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.67% | **+1.67%** |
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.94% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.60% | **+0.57%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.57% | **+0.46%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.28% | **+0.45%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.36% | **+0.12%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$841.06** / 初期 $100.00 (+741.06%)
- 確定: 5137件 (Win 1539 / Loss 1680 / Flat 1918) / skip 5288件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAN/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $841.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2571件 (Win 717 / Loss 618 / Flat 1236) / skip 4704件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0574 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.22** / 初期 $100.00 (+19.22%)
- 確定: 2456件 (Win 729 / Loss 935 / Flat 792) / pending 4件 / skip 2875件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XAN/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $119.22

## 6. Latest Market Context

- 更新: 2026-09-07T07:11:08.017668+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=79636.6
- Funnel: target 1059 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +212.95% | $1,271,411.53 |
| BONER/USDT:USDT | +127.00% | $5,095,190.56 |
| XAN/USDT:USDT | +11.95% | $2,234,947.48 |
| UAI/USDT:USDT | +11.70% | $14,427,492.93 |
| KAS/USDT:USDT | +11.49% | $4,084,635.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +2.37% | +2.34% |
| UAI/USDT:USDT | below_1h_threshold | +1.92% | +1.90% |
| ICP/USDT:USDT | below_1h_threshold | +0.99% | +0.96% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.79% | +0.76% |
| METIS/USDT:USDT | below_1h_threshold | +0.69% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
