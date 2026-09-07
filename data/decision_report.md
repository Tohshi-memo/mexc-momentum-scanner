# Decision Report

- generated_at: 2026-09-07T03:01:21.710355+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13856**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.39% / filled 20/20。**
- 全期間 MARKET基準: n=13856, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +7.39% | **+2.59%** |
| LIMIT_7PCT | 7/20 | 35.0% | +6.52% | **+2.28%** |
| LIMIT_9PCT | 6/20 | 30.0% | +7.43% | **+2.23%** |
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_BB3S | 4/13 | 30.8% | +3.06% | **+0.94%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.72% | **+0.69%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.49% | **+0.45%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.42% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$841.06** / 初期 $100.00 (+741.06%)
- 確定: 5130件 (Win 1539 / Loss 1680 / Flat 1911) / skip 5287件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $841.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2570件 (Win 717 / Loss 618 / Flat 1235) / skip 4697件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0405 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.22** / 初期 $100.00 (+19.22%)
- 確定: 2450件 (Win 729 / Loss 935 / Flat 786) / pending 4件 / skip 2875件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000265 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $119.22

## 6. Latest Market Context

- 更新: 2026-09-07T03:01:11.680247+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=79808.2
- Funnel: target 1059 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +188.49% | $4,002,625.49 |
| UAI/USDT:USDT | +16.94% | $12,580,728.74 |
| XAN/USDT:USDT | +12.54% | $1,533,977.20 |
| TIA/USDT:USDT | +10.88% | $17,980,515.49 |
| TAO/USDT:USDT | +10.29% | $82,152,834.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTER/USDT:USDT | below_1h_threshold | +0.34% | +0.39% |
| UNI/USDT:USDT | below_1h_threshold | +0.27% | +0.31% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.24% | +0.29% |
| ONDO/USDT:USDT | below_1h_threshold | +0.21% | +0.25% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.18% | +0.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
