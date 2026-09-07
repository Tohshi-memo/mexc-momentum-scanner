# Decision Report

- generated_at: 2026-09-07T05:26:23.732867+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13862**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.77% / filled 20/20。**
- 全期間 MARKET基準: n=13862, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.77% | **+1.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.13% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.81% | **+0.69%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.49% | **+0.45%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.53% | **+0.19%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.12% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$841.06** / 初期 $100.00 (+741.06%)
- 確定: 5135件 (Win 1539 / Loss 1680 / Flat 1916) / skip 5288件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CRV/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $841.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2570件 (Win 717 / Loss 618 / Flat 1235) / skip 4703件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0561 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.22** / 初期 $100.00 (+19.22%)
- 確定: 2454件 (Win 729 / Loss 935 / Flat 790) / pending 4件 / skip 2875件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $119.22

## 6. Latest Market Context

- 更新: 2026-09-07T05:26:11.486242+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=79869.4
- Funnel: target 1059 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +173.08% | $1,085,694.30 |
| BONER/USDT:USDT | +135.96% | $4,632,615.13 |
| XAN/USDT:USDT | +18.65% | $1,912,814.27 |
| AKE/USDT:USDT | +10.73% | $8,059,911.49 |
| TAO/USDT:USDT | +10.36% | $95,452,910.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| METIS/USDT:USDT | below_1h_threshold | +2.94% | +2.71% |
| ICP/USDT:USDT | below_1h_threshold | +2.64% | +2.41% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.98% | +1.75% |
| LINK/USDT:USDT | below_1h_threshold | +1.94% | +1.71% |
| SUI/USDT:USDT | below_1h_threshold | +1.65% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
